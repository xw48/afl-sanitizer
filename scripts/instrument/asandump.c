#ifndef __M_ASAN_DUMP_FILE_
#define __M_ASAN_DUMP_FILE_
#include <sanitizer/asan_interface.h>

void __attribute__((destructor)) asanEnd(void);
void __attribute__((destructor)) asanEnd(void) {
    __xw48_asan_print_accumulated_stats();
}

#endif
