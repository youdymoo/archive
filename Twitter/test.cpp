#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>

using namespace std;

string hacking_time() {
    vector<int> key{8, 2, 5, 1, 2, 2, 0};
    string encrypted_message = "Otjfvknou, kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg";
    string original_message;
    char letter;
    int key_count = 0;
    for (int i = 0; i != (int) encrypted_message.size(); ++i) {
        if ((encrypted_message[i] >= 'a' && encrypted_message[i] <= 'z') || (encrypted_message[i] >= 'A' && encrypted_message[i] <= 'Z')) {
            letter = (char) (encrypted_message[i] - key[key_count]);
            if (letter < 'A' || (letter < 'a' && letter > 'Z') ) {
                letter += 26;
            }

            key_count = (key_count + 1) % 7;
            original_message += letter;
        } else
            original_message += encrypted_message[i];
    }
    cout << original_message << endl;
    return original_message;
}

int main() {
    hacking_time();
}
