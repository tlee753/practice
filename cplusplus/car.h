// class structure
// function declarations

#include <iostream>
#include <string>
using namespace std;

#ifndef car_H
#define car_H

class car {
    public:
        car(); // default constructor
        // ~car(); // destructor

        car(string, int, string); // overload constructor

        // member variables
        string make;
        int year;
        string color;
};

#endif