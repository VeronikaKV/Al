// синхронизация.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"


int main()
{
	auto in_file = std::ifstream(INPUT_FILE);
	std::ofstream out_file = std::ofstream(OUTPUT_FILE);

	int N, M, R;
	in_file >> N;
	vector<int> Ai(N);

	for (int i=0; i < N; i++) { in_file >> Ai[i];}
	in_file >> M;
	vector<int> Bi(M);
	for (int i = 0; i < M; i++) { in_file >> Bi[i]; }
	vector<int> rasnostA(N);
	rasnostA[0] = 0;
	for (int i = 1; i < N; i++) 
	{
		R = Ai[i] - Ai[i - 1];
		rasnostA[i] = R;
	}

	for (int i = 0; i < N - M; i++)
	{
		vector< int > ivec(&rasnostA[i], &rasnostA[i + M]);
		ivec[0] = 0;
		if (ivec == Bi) { out_file << (i + 1);   return(0); }
		ivec.clear();
	}

}

