#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream iFile;
    iFile.open(argv[1]);
    if(!iFile)
    {
        cerr << "Cannot open " << argv[1] << endl;
        return -1;
    }
    
    string line;
    while(getline(iFile, line))
    {
        cout << line << endl;
    }

    return 0;
}
