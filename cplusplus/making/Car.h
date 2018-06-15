#include <iostream>
#include <string>

using namespace std;

#ifndef CAR_H
#define CAR_H

class Car {
    public:
        string make;
        string model;
        int  year;

        Car();
        Car(string, string, int);
};

#endif
