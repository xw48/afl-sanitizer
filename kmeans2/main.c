#include "k-means.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_LOOPS 10
int main (void) {
	double data_points[] = {1.0, 2.0, 0.5, 0.3, 0, 0.19, 0, 0.15, 0.13, 0.24, 0.76, 0.25, 0.3, 0.76, 0.06, 1, 1, 0, 1, 0.76, 0.5, 1, 0.76, 0.5, 0.7, 0.76, 0.25, 1, 1, 0.5, 1, 1, 0.25, 1, 1, 0.5, 0.7, 0.76, 0.5, 0.7, 0.68, 1, 1, 1, 0.5};
	int num_points = 15;
	int dim = 3;
	int num_clusters = 3;
	srand(time(NULL));

	int* seed_map = (int *) calloc(num_points, sizeof(int));

	int i;
	for (i = 0; i < MAX_LOOPS; ++i) {
		double** centroids = (double ** ) calloc(num_clusters, sizeof(double *));
		int j;
		for (j = 0; j < num_clusters; ++j) {
			centroids[j] = (double * ) calloc(dim, sizeof(double));
		}

		j = 0;
		memset(seed_map, '\0', num_points * sizeof(int));
		while (1) {
			int r = rand() % num_points;
			if (!seed_map[r]) {
				seed_map[r]++;

				if (j >= num_clusters) {
					break;
				}
				memcpy(centroids[j], data_points + r * dim, dim * sizeof(double));
				++j;
			}
		}

		int *c = k_means(num_points, dim, data_points, num_clusters, 1e-4, centroids);
		for (j = 0; j < num_clusters; ++j) {
			printf("centroid %d: %.1f, %.1f, %.1f\n", j, centroids[j][0], centroids[j][1], centroids[j][2]);
		}

		for (j = 0; j < num_points; j++) {
			printf("data point %d is in cluster %d\n", j, c[j]);
		}

		free(c);
		for (j = 0; j < num_clusters; ++j) {
			free(centroids[j]);
		}
		free(centroids);
	}

	free(seed_map);

	return 0;
}