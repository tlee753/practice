#include <string>
#include "Car.h"

Car::Car() {
    this->make = "unknown";
    this->model = "unknown";
    this->year = 0;
}

Car::Car(string make, string model, int year) {
    this->make = make;
    this->model = model;
    this->year = year;
}
