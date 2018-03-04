#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int longest_phrase_in_tweet() {
   vector<int> tweet;
   queue<int> phrase;
   int input;
   while (cin >> input && input != -1) {
       tweet.push_back(input);
   }

   int limit = 3;
   int maxlength = 0;
   int sum = 0;
   for (int i = 0; i != (int) tweet.size(); ++i) {
       phrase.push(tweet[i]);
       sum++;
       if (sum >= limit) {
           sum--;
           phrase.pop();
       }
       if (sum > maxlength)
           maxlength = sum;
   }

   cout << "output: " << maxlength << endl;
}

//int KGame() {
//    int m = 8, k = 6;
//    int n = k + m;
//    vector<vector<int>> c((unsigned) (n + 1), vector<int>((unsigned) (m + 1)));
//    for (int j = 0; j <= m; j++) {
//        for (int i = j; i <= n; i++) {
//            if ((i == j) || (j == 0))
//                c[i][j] = 1;
//            else
//                c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
//        }
//    }
//    cout << c[n][m] << endl;
//    return 0;
//}
//
//int numberOfPaths(int m, int n) {
//    int count[m][n];
//    for (int i = 0; i < m; i++)
//        count[i][0] = 1;
//    for (int j = 0; j < n; j++)
//        count[0][j] = 1;
//
//    for (int i = 1; i < m; i++) {
//        for (int j = 1; j < n; j++)
//            count[i][j] = count[i - 1][j] + count[i][j - 1];
//    }
//    return count[m - 1][n - 1];
//}

//bool if_valid_email(char letter);
//
//int main() {
//    string input = "E:     think@twitter. com";
//    string output = "E:";
//    while (input[0] != '0') {
//        if (input[0] == 'E') {
//            int i = 2;
//            cout << input << endl;
//            while (!if_valid_email(input[i])) {
//                char k = input[i];
//                ++i;
//            }
//            char k = input[i];
//            output += input[i];
//            while (input[i+1] != '@') {
//                if (if_valid_email(input[i]))
//                    output += "*";
//                ++i;
//            }
//            output += input.substr(i);
//            cout << output << endl;
//        }
//        cin >> input;
//    }
//}
//
//bool if_valid_email(char letter) {
//    return ((int) letter >= 94 && (int) letter <= 126) || ((int) letter >= 65 && (int) letter <= 90) ||
//           ((int) letter >= 35 && (int) letter <= 39) || ((int) letter >= 42 && (int) letter <= 45) ||
//           (int) letter == 33;
//}