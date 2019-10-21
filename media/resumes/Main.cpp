#include <iostream>
#include <stdexcept>
using namespace std;

class Color {
/* Public */
public:
    void cout_rgb (void) { cout << "Color Values: (" << R << ',' << G <<
        ',' << B << ')' << endl;}
	int get_R(){return R;}
	int get_G(){return G;}
	int get_B(){return B;}
	void set_R(int Red){
		if (Red > 255 || Red < 0)
			throw runtime_error{"Out of range"};
		R = Red;
		}
	void set_G(int Green){
		if (Green > 255 || Green < 0)
			throw runtime_error{"Out of range"};
		G = Green;
		}
	void set_B(int Blue){
		if (Blue > 255 || Blue < 0)
			throw runtime_error{"Out of range"};
		B = Blue;
		}
/* Private */
private:
	int R = 255;
    int G = 255;
    int B = 255;
};

int main()
{
    Color color;
    color.cout_rgb();
	cout << "color.R = " << color.get_R() << endl;
	cout << "color.G = " << color.get_G() << endl;
	cout << "color.B = " << color.get_B() << endl;
	
	cout << "Please enter integer values for R, G, and B: ";
	int R,G,B;
	cin >> R >> G >> B;
	try{
		color.set_R(R); color.set_G(G); color.set_B(B);
	}
	catch (runtime_error){
		cout << "the value is out of range" << endl;;
		return 1;
	}
	color.cout_rgb();
}