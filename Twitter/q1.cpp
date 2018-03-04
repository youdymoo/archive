#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;


vector<int> getRecommendedTweets(vector<tuple<int, int>> followGraph_edges,
                                vector <tuple<int, int>> likeGraph_edges,
                                int targetUser,
                                int minLikeThreshold);

vector<int> getRecommendedTweets(vector<tuple<int, int>> followGraph_edges,
                        vector <tuple<int, int>> likeGraph_edges,
                        int targetUser,
                        int minLikeThreshold)  {
   unordered_map<int, int> follow_map;
   unordered_map<int, int> like_map;
   vector<int> tweets;

   for (int i = 0; i != (int) followGraph_edges.size(); ++i) {
       auto follow_edge = followGraph_edges[i];
       if (get<0>(follow_edge) == targetUser) {
           follow_map[get<1>(follow_edge)] = 1;
       }
   }

   for (int i = 0; i != (int) likeGraph_edges.size(); ++i) {
       auto like_edge = likeGraph_edges[i];
       if (follow_map[get<0>(like_edge)] == 1) {
           like_map[get<1>(like_edge)]++;
       }
   }

   for (auto it: like_map) {
       if (it.second >= minLikeThreshold)
           tweets.push_back(it.first);
   }

   std::sort(tweets.begin(), tweets.end());
   return tweets;
}

int main() {
   vector<tuple<int, int>> followGraph_edges;
   vector<tuple<int, int>> likeGraph_edges;
   int targetUser = 1;
   int minLikeThreshold = 2;
   followGraph_edges.push_back(make_tuple(1, 2));
   followGraph_edges.push_back(make_tuple(1, 3));
   followGraph_edges.push_back(make_tuple(2, 3));
   likeGraph_edges.push_back(make_tuple(1, 1));
   likeGraph_edges.push_back(make_tuple(2, 2));
   likeGraph_edges.push_back(make_tuple(1, 2));
   likeGraph_edges.push_back(make_tuple(3, 2));
   likeGraph_edges.push_back(make_tuple(2, 4));
   likeGraph_edges.push_back(make_tuple(3, 4));
   vector<int> res = getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold);
   for (int i = 0; i < res.size(); i++) {
       cout << res[i] << endl;
   }
}
