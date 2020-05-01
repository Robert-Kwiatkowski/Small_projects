#include <iostream>
#include <string>
#include <exception>

class E : public std::exception {
    const char * msg;
    E(){};
public:
    explicit E(const char * s) throw() : msg(s) {}
    const char * what() const throw() {return msg;}
};

template <typename T> class stack {
static const int defsize = 10;
static const int maxsize = 100;
int _size;
int _top;
T * _stkptr;

public:
    explicit stack(int s = defsize);
    ~stack() {delete [] _stkptr;}
    T & push(const T &);
    T & pop();
    bool isempty() {return _top < 0;}
    bool isfull() {return _top == _size-1;}
    int top() {return _top;}
    int size() {return _size;}


};
template<typename T>
stack<T>::stack(int s) {
    if (s < 1 || s > maxsize)
        throw E("Invalid stack size");
    else
        _size = s;
    _stkptr = new T[_size];
    _top = -1;

}
template<typename T>
T & stack<T>::push(const T & i) {
    if(isfull())
        throw E("Stack is full");
    return _stkptr[++_top] = i;
}

template<typename T>
T & stack<T>::pop() {
    if(isempty())
        throw E("Stack is empty");
    return _stkptr[_top--];

}

int main() {
    try {
        stack<int> si(8);
        for (int i : {1, 2, 3, 4, 5, 6, 7, 8}) {
            si.push(i);
            std::cout <<"Pushed " << i << " inside the stack" << std::endl;
        }
        while(!si.isempty()){
            std::cout <<"Popped " << si.pop() << " out of the stack" << std::endl;
        }
    }
    catch (E & e) {
        std::cout << "Stack error: " << e.what() << std::endl;
    }

    try {
        stack<std::string> si(3);
        for (std::string i : {"one", "two", "three"}) {
            si.push(i);
            std::cout <<"Pushed " << i << " inside the stack" << std::endl;
        }
        while(!si.isempty()){
            std::cout <<"Popped " << si.pop() << " out of the stack" << std::endl;
        }
    }
    catch (E & e) {
        std::cout << "Stack error: " << e.what() << std::endl;
    }
}
