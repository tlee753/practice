#include <iostream>

using namespace std;

void func (int *ptr) {
	*ptr = 30;
	//cout << "testing" << *ptr << endl;
}

int main() {
	int var = 0;
	int *ptr = &var;
	
	func(ptr);

	cout << var << endl;
	
	return 0;
}
