#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

//int longest_phrase_in_tweet() {
//    vector<int> tweet;
//    queue<int> phrase;
//    int input;
//    while (cin >> input && input != -1) {
//        tweet.push_back(input);
//    }
//
//    int limit = 3;
//    int maxlength = 0;
//    int sum = 0;
//    for (int i = 0; i != (int) tweet.size(); ++i) {
//        phrase.push(tweet[i]);
//        sum++;
//        if (sum >= limit) {
//            sum--;
//            phrase.pop();
//        }
//        if (sum > maxlength)
//            maxlength = sum;
//    }
//
//    cout << "output: " << maxlength << endl;
//}

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

//#include <map>
//#include <algorithm>
//
//vector<int> getRecommendedTweets(vector<tuple<int, int>> followGraph_edges,
//                                 vector <tuple<int, int>> likeGraph_edges,
//                                 int targetUser,
//                                 int minLikeThreshold);
//
//vector<int> getRecommendedTweets(vector<tuple<int, int>> followGraph_edges,
//                         vector <tuple<int, int>> likeGraph_edges,
//                         int targetUser,
//                         int minLikeThreshold)  {
//    unordered_map<int, int> follow_map;
//    unordered_map<int, int> like_map;
//    vector<int> tweets;
//
//    for (int i = 0; i != (int) followGraph_edges.size(); ++i) {
//        auto follow_edge = followGraph_edges[i];
//        if (get<0>(follow_edge) == targetUser) {
//            follow_map[get<1>(follow_edge)] = 1;
//        }
//    }
//
//    for (int i = 0; i != (int) likeGraph_edges.size(); ++i) {
//        auto like_edge = likeGraph_edges[i];
//        if (follow_map[get<0>(like_edge)] == 1) {
//            like_map[get<1>(like_edge)]++;
//        }
//    }
//
//    for (auto it: like_map) {
//        if (it.second >= minLikeThreshold)
//            tweets.push_back(it.first);
//    }
//
//    std::sort(tweets.begin(), tweets.end());
//    return tweets;
//}

int main() {
//    vector<tuple<int, int>> followGraph_edges;
//    vector<tuple<int, int>> likeGraph_edges;
//    int targetUser = 1;
//    int minLikeThreshold = 2;
//    followGraph_edges.push_back(make_tuple(1, 2));
//    followGraph_edges.push_back(make_tuple(1, 3));
//    followGraph_edges.push_back(make_tuple(2, 3));
//    likeGraph_edges.push_back(make_tuple(1, 1));
//    likeGraph_edges.push_back(make_tuple(2, 2));
//    likeGraph_edges.push_back(make_tuple(1, 2));
//    likeGraph_edges.push_back(make_tuple(3, 2));
//    likeGraph_edges.push_back(make_tuple(2, 4));
//    likeGraph_edges.push_back(make_tuple(3, 4));
//    vector<int> res = getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold);
//    for (int i = 0; i < res.size(); i++) {
//        cout << res[i] << endl;
//    }
    hacking_time();
}
