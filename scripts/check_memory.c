#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>

#define MEM_SHM_ENV_VAR     "__AFL_MEM_SHM_ID"

int main(int argc, char* argv[]) {
  unsigned long long *mem;
  char mem_str[4096];

  char shm_str[16];
  int shm_id = shmget(IPC_PRIVATE, 256 * sizeof(unsigned long long), IPC_CREAT | IPC_EXCL | 0600);

  if (shm_id < 0) {
    printf("shmget failed\n");
    return -1;
  }

  mem = (unsigned long long *) shmat(shm_id, NULL, 0);
  if (!mem) {
    printf("shmat failed\n");
    return -1;
  }
  memset(mem, '\0', 256 * sizeof(unsigned long long));

  sprintf(shm_str, "%d", shm_id);
  setenv(MEM_SHM_ENV_VAR, shm_str, 1);

  pid_t pid = fork();
  if (pid < 0) {
    exit(-1);
  }

  if (!pid) {
    //child process
    char mem_profile_env[128];
    sprintf(mem_profile_env, "PROFILE%d", getpid());
    setenv(mem_profile_env, "show=1", 1);

    execv(argv[1], argv+1);
    exit(1);
  } else {
    int status;
    waitpid(-1, &status, 0);

    int i = 0;
    for (;i < 256; ++i) {
      sprintf(mem_str + strlen(mem_str), "%d,", mem[i]);
    }
    printf("mem trace: %s\n", mem_str);
  }
  return 0;
}
