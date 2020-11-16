#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

// for convenience
using json = nlohmann::json;

using namespace std;

//Design Decision: 
//Average should handle all the calculations needed to find the average, this includes the summation 
unsigned int average(unsigned int n1,unsigned int n2){
    unsigned int mean;
    mean = (n1 + n2)/2;
    return mean;
}

unsigned long long average(vector<unsigned int> nValues){
    if(nValues.size() == 0){
        return 0;
    } 
    unsigned long long mean = 0;
    for(auto element : nValues){
        mean += element;
    }
    mean /= nValues.size();
    return mean;
}

unsigned int strCleaner(string str){
    unsigned int na = 0;
    string temp;
    if(str == "N/A"){
        return na;
    }
    for(auto element : str){
        if(element == '$' || element == ',' || element == ' ' || element == '"'){
            continue;
        }
       temp += element;
    }
    cout << temp << endl;
    int newStr = stoi(temp);
    return (unsigned int)newStr;
}

void top10(){
    string l_cities [10] = {"newyork - ny",
        "los-angeles-ca",
        "san-francisco-ca",
        "denver-co",
        "washington-dc", 
        "miami-fl",
        "chicago-il",
        "dallas-tx",
        "austin-tx",
        "boulder-co"};

    ifstream myfile1("mappedzips.json");
    ifstream myfile2("fileZ.json");
    json j, zips, records;

    myfile1 >> j;
    myfile2 >> zips;
    for(string city : l_cities){
        auto holder = j[city];
        vector<unsigned int> summation;
        for(string zip: holder){
            summation.push_back(zips[zip]);
        }
        auto mean = average(summation);
        records[city] = mean;
    }
    
    ofstream outputfile("city10mean_wk10.json");
    outputfile<< setw(4) << records << endl;
}
int main(void)
{
    string line;
    ifstream my_json("records_v10.json");
    ifstream zips("zip_set_10.txt");
    json my_stat;
    json j;
    my_json >> j;
    while(getline(zips,line)){
        vector<unsigned int> summation; 
        auto map = j[line];
        for(auto element: map){
            string element_str = element.dump();
            size_t result = element_str.find("-");
            if(result != string::npos){
                string n1, n2;
                for (int i = 0; i < element_str.size(); i++)
                {
                    if(i < result){
                        n1 += element_str[i];
                    }
                    if(i > result){
                        n2 += element_str[i];
                    }
                }
               auto mean = average(strCleaner(n1),strCleaner(n2));
               summation.push_back(mean);

            }else if(element_str != "N/A"){
                continue;
                
            }else{
                unsigned int cleanedInt = strCleaner(element);
                summation.push_back(cleanedInt);
            }
        }
        auto city_mean = average(summation);
        my_stat[line] = city_mean; 
    
    }

    ofstream f_myrecord("fileZ.json");
    f_myrecord << setw(4) << my_stat << endl;

    top10();
    return 0;
}
    // for(auto item: j){
    //     cout << item << endl;
    // }
    // auto filt = "75287";
    // cout << j[filt];
    // return 0;
    //Open file
    //Read json
    // for(auto line:  json){
    //     for()
    // }
