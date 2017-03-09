#include <iostream>
#include <string>
using namespace std;

// classes
#include "car.h"

// function prototypes
void question();
void pointer();

// main
int main() {

    car mustang = new car; // use  constructor

    cout << mustang.year;
    return 0;
}

// functions
void question() {
    string question = "What is your favorite color?"; // initialize and assign question string
    string answer; // initialize answer type

    cout << question << "\n" << "ans: "; // output question with answer prompt
    cin >> answer; // get user input
    cout << "Your favorite color is " << answer << ".\n"; // outputs formulate response
}

void pointer() {
    int *ptr;
    cout << "Pointer Memory Location is " << ptr << "\n";
}

