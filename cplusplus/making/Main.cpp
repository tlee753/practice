#include <iostream>
#include "Car.h"

using namespace std;

int main() {
    cout << "hello world" << endl;
    Car* myCar = new Car("Ford", "Mustang", 1997);
    cout << myCar->make << endl;
    return 0;
}
