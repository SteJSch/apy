// helloWorld.h file
#include <vector>

class important_class {
	
 public :
  important_class();
  ~important_class();
  double mymethod();
  void tell_me();
 private : 
  double some_var;
  
};

extern "C" {
    important_class* important_class_new(){ return new important_class(); }
    double important_class_fun(important_class* myclass){ return myclass->mymethod(); }
    void important_class_speak(important_class* myclass){ myclass->tell_me(); }
}
