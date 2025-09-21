#include <iostream>
#include <string>
using namespace std;

struct Food {
    string name;
    string cuisine;
    int rating;
};

class FoodRatings {
    Food foods[100];     // max 100 foods for simplicity
    int n;

public:
    FoodRatings(string names[], string cuisines[], int ratings[], int size) {
        n = size;
        for (int i = 0; i < n; i++) {
            foods[i].name = names[i];
            foods[i].cuisine = cuisines[i];
            foods[i].rating = ratings[i];
        }
    }

    void changeRating(string food, int newRating) {
        for (int i = 0; i < n; i++) {
            if (foods[i].name == food) {
                foods[i].rating = newRating;
                break;
            }
        }
    }

    string highestRated(string cuisine) {
        string bestFood = "";
        int bestRating = -1;
        for (int i = 0; i < n; i++) {
            if (foods[i].cuisine == cuisine) {
                if (foods[i].rating > bestRating || 
                   (foods[i].rating == bestRating && foods[i].name < bestFood)) {
                    bestRating = foods[i].rating;
                    bestFood = foods[i].name;
                }
            }
        }
        return bestFood;
    }
};

int main() {
    string foods[] = {"kimchi","miso","sushi","moussaka","ramen","bulgogi"};
    string cuisines[] = {"korean","japanese","japanese","greek","japanese","korean"};
    int ratings[] = {9,12,8,15,14,7};
    int size = 6;

    FoodRatings fr(foods, cuisines, ratings, size);

    cout << fr.highestRated("korean") << endl;   // kimchi
    cout << fr.highestRated("japanese") << endl; // ramen

    fr.changeRating("sushi", 16);
    cout << fr.highestRated("japanese") << endl; // sushi

    fr.changeRating("ramen", 16);
    cout << fr.highestRated("japanese") << endl; // ramen

    return 0;
}
