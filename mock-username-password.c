#include <iostream>
#include <string>

using namespace std; 	//introduces namespace std
int main( void )
{
    int password;
    password = 1234;

    string username;
    username = 'Raymond';
    string userinput;

    do
	{
        cout << "Enter username:";
	    cin >> userinput;
	    if (userinput == username);
        {
	        cout <<"\n";
	        cout << "Enter password:";
	        cin >> password;
	    }
 	}
	while (userinput == username);
        if (password == 1234)
            cout << "Access Granted...";
        if (password != 1234)
            cout << "Access Denied.....Invalid Username/Password:";
    return 0;
}