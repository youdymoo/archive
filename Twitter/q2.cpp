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
