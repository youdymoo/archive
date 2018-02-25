#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdint>

using namespace std;

struct stream_type {
    // for part 1
    int total_pixals;
    int ones;
    int zeros;
    // for part 2
    vector<bool> chain;
    // for part 3
    vector<uint64_t> encoding;
    vector<uint64_t> re_encoding;

    stream_type() {
        this->total_pixals = 0;
        this->ones = 0;
        this->zeros = 0;
    }
};

int main(/*int argc, char *argv[]*/) {
    // data structure
    vector<stream_type *> storage(4);
    for (int i = 0; i < 4; ++i) {
        stream_type *s = new stream_type;
        storage[i] = s;
    }

    // load a file
    string fileName;
    //fileName = argv[1];
    fileName = "stream-data.txt";
    ifstream filePtr;
    filePtr.open(fileName);

    if (!filePtr) {
        cerr << "Fail to open file: " << fileName << "\n";
        exit(1);
    }

    // read a file
    string line;
    int stream_index, stream_sequences, stream_num;
    while (getline(filePtr, line)) {
        stringstream input(line);
        input >> stream_index >> stream_sequences >> stream_num;
        storage[stream_index]->total_pixals += stream_sequences;
        if (stream_num) {
            for (int j = 0; j < stream_sequences; ++j)
                storage[stream_index]->chain.push_back(true);
            storage[stream_index]->ones += stream_sequences;
        } else {
            for (int j = 0; j < stream_sequences; ++j)
                storage[stream_index]->chain.push_back(false);
            storage[stream_index]->zeros += stream_sequences;
        }
    }

    cout << "------part-1------\n";

    // output of part1
    int all_pixals = 0;
    for (int i = 0; i < 4; ++i) {
        string output = "Stream #" + to_string(i);
        all_pixals += storage[i]->total_pixals;
        output += ": <" + to_string(storage[i]->total_pixals) + "> total pixals";
        output += ", <" + to_string(storage[i]->ones) + "> ones";
        output += ", <" + to_string(storage[i]->zeros) + "> zeros\n";
        cout << output;
    }

    int division = all_pixals / 100;
    cout << "\nImage Height: " << division << " pixels\n";

    cout << "------part-2------\n";

    // output of part2
    cout << "P1\n";
    cout << division << " 100\n";
    uint8_t count = 0;
    for (int i = 0; i < division; ++i) {
        string output_line;
        // 25 is 100 / 4
        for (int j = 0; j < 25; ++j) {
            for (int k = 0; k < 4; ++k)
                output_line += to_string(storage[k]->chain[count]);
            count++;
        }
        cout << output_line << "\n";
    }

    /*
     the current encoding method is convenient for stream to store but not that convenient for computers to present
     because the streams' vertical reading order. that's the main reason i chose the vector<bool> as the output helper.

     now we use three integers (maybe shorter-bit number like short) to represent a sequence in the picture but it's
     not suitable for those pics that have frequent black-white change (from 1 to 0, then 0 to 1), which would be
     stored as #stream 1 1\n #stream 1 0\n...(example).

     my first idea is to only record the change point and set the default start as 0 (if stream starts from 1 then the
     first turning point is 0). so we can save 1/3 of the space compared to the original encoding method. but it still
     couldn't resist the frequently changing case as mentioned above.

     so my re-encoding is to use a certain number (decided by the vertical length of the picture) of uint64_t to
     encode. all the bits are directly recorded into the bits of the numbers. if the 64 bits are used up, start a new
     uint64_t and push the former one into the storage vector. without considering the turning point, it would even
     be easier for computers to decode.
     */

    cout << "------part-3------\n";

    uint8_t re_encode_helper[4] = {0, 0, 0, 0};
    uint64_t re_encode_record[4] = {0, 0, 0, 0};
    // re-encode from the boolean vector
    for (int k = 0; k < 4; ++k) {
        re_encode_helper[0] = 0;
        re_encode_record[0] = 0;
        //cout << "Stream #" << k << ": ";
        for (auto c: storage[k]->chain) {
            re_encode_helper[0]++;
            if (c)
                re_encode_record[0] = (re_encode_record[0] << 1) + 1;
            else
                re_encode_record[0] = (re_encode_record[0] << 1);

            if (re_encode_helper[0] == 62) {
                storage[k]->encoding.push_back(re_encode_record[0]);
                cout << re_encode_record[0] << " ";
                re_encode_record[0] = 0;
                re_encode_helper[0] = 0;
            }
        }
        cout << "\n";
    }

    // back to file beginning
    filePtr.clear();
    filePtr.seekg(0, ios::beg);

    // re-encode from the file
    re_encode_helper[0] = 0;
    re_encode_record[0] = 0;
    while (getline(filePtr, line)) {
        stringstream input(line);
        input >> stream_index >> stream_sequences >> stream_num;
        if (stream_num) {
            for (int i = 0; i < stream_sequences; ++i) {
                re_encode_helper[stream_index] += 1;
                re_encode_record[stream_index] = re_encode_record[stream_index] << 1;
                re_encode_record[stream_index] += 1;

                if (re_encode_helper[stream_index] == 62) {
                    storage[stream_index]->re_encoding.push_back(re_encode_record[stream_index]);
                    re_encode_record[stream_index] = 0;
                    re_encode_helper[stream_index] = 0;
                }
            }
        } else {
            for (int i = 0; i < stream_sequences; ++i) {
                re_encode_record[stream_index] = (re_encode_record[stream_index] << 1);

                if (re_encode_helper[stream_index] == 62) {
                    storage[stream_index]->re_encoding.push_back(re_encode_record[stream_index]);
                    re_encode_record[stream_index] = 0;
                    re_encode_helper[stream_index] = 0;
                }
            }
        }
    }


    // close the file
    filePtr.close();

    // delete the stream objects
    for (int i = 0; i < 4; ++i) {
        delete (storage.back());
        storage.back() = nullptr;
        storage.pop_back();
    }

    return 0;
}

