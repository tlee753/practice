#include <iostream>
#include <time.h>

using namespace std;

//__global__
void sumation (int max, int * sum) {
	for (int i = 1; i <= max; i++) {
		sum += i;
	}
}


int main() {
	clock_t t1, t2;
	t1 = clock();
	
	cout << "Program started..." << endl;
	int x = 1000000;
	int *sum = 0;

	// cudaMallocManaged(&sum, sizeof(int));

	// cout << "Pick a number to sum: " << endl;
	// cin >> x;
	
	sumation(x, sum);
	// cudaDeviceSynchronize();
	
	cout << "Sum is " << sum << "." << endl;
	
	t2 = clock();
	float diff = (float)t2 - (float)t1;
	float seconds = diff/ CLOCKS_PER_SEC;
	cout << "Program time is " << seconds << "." << endl;

	return 0;
}

