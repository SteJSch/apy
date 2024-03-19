
// helloWorld.cpp file
#include <iostream>
#include "../include/fourier.h"

important_class::important_class() {
 this->some_var = 3.3;
}

important_class::~important_class() {
};

double important_class::mymethod() {
 return this->some_var;
};

void important_class::tell_me() {
 std::cout << "val is " << this->some_var << std::endl;
};
