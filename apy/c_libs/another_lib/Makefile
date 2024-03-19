libfourier.o : fourier.o
	g++ fourier.o -shared -o lib/fourier.so

fourier.o : src/fourier.cpp include/fourier.h
	g++ -c -fPIC src/fourier.cpp -o fourier.o

clean : 
	rm -f *.o
