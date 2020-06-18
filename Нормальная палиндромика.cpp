// Ќормальна€ палиндромика.cpp: определ€ет точку входа дл€ консольного приложени€.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	ifstream in_file = ifstream("input.txt");
	ofstream out_file = ofstream("output.txt");

	string s1;
	std::getline(in_file, s1);
	int l = s1.length();
	string s = s1;
	reverse(s1.begin(), s1.end());
	vector<int> nul(l, 0);
	vector< char > k1;
	vector< char > k;

	int h = 1;
	if (s != s1) { h = 0; }
	if (h == 1) { out_file << ""; return(0); }

	for (int i = 0; i < l - 1; i++)
	{
		k.emplace_back(s1[i]);
		reverse(k.begin(), k.end());
		k1 = k;
		reverse(k.begin(), k.end());
		if (k != k1) { nul[i] = 0; }
		else { nul[i] = 1; }
	}
	reverse(nul.begin(), nul.end());
	for (int i = 0; i <l; i++) {
		if (nul[i] != 0) {
			h = i;
			break;
		}
	}
	s.erase(s.begin() + h, s.end());
	reverse(s.begin(), s.end());
	out_file << s;

	return(0);
}