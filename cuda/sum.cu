#include <iostream>
#include <iomanip>
#include <time.h>

using namespace std;

__global__
void sumation (int max, int *sumPtr) {
	printf("%d\n", max);
	for (int i = 1; i <= max; i++) {
		*sumPtr += i;
		printf("%d\n", *sumPtr);
	}
}

int main() {
	clock_t t1, t2;
	t1 = clock();
	
	cout << "Program started..." << endl;
	int x = 800, sum = 0;
	int *sumPtr = &sum;
	
	cudaMallocManaged(&sumPtr, sizeof(int));
	
	// cout << "Pick a number to sum: " << endl;
	// cin >> x;
	
	sumation<<<1, 256>>>(x, sumPtr);
	cudaDeviceSynchronize();
	
	cout << "Sum is " << sum << "." << endl;
	
	t2 = clock();
	float diff = (float)t2 - (float)t1;
	float seconds = diff/ CLOCKS_PER_SEC;
	cout << "Program time is " << seconds << "." << endl;
	
	cudaFree(sumPtr);
	
	return 0;
}
