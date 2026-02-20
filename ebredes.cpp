#include <iostream>
#include <string>
using namespace std;

struct NapAdat {
    string nap;
    string ebredesiIdo;
};

int main() {
    NapAdat het[7] = {
        {"Hetfo:", "06:30"},
        {"Kedd:", "06:45"},
        {"Szerda:", "06:30"},
        {"Csutortok:", "07:00"},
        {"Pentek:", "06:15"},
        {"Szombat:", "08:30"},
        {"Vasarnap:", "09:00"}
    };

    cout << "Heti ebredesi idok:\n\n";

    for (int i = 0; i < 7; i++) {
        cout << het[i].nap  
                  << het[i].ebredesiIdo 
                  << endl;
    }

    return 0;
}
