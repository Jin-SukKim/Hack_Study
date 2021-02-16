int sub_1400010C0(char arg1) {
	int tmp1 = 0;
	switch(arg1) {
		case 0x65: tmp1 = 3; break; // e
		case 0x69: tmp1 = 8; break; // i
		case 0x6f: tmp1 = 9; break; // o
		case 0x70: tmp1 = 0; break; // p
		case 0x71: tmp1 = 1; break; // q
		case 0x72: tmp1 = 4; break; // r
		case 0x74: tmp1 = 5; break; // t
		case 0x75: tmp1 = 7; break; // u
		case 0x77: tmp1 = 2; break; // w
		case 0x79: tmp1 = 6; break; // y
		default: {
			sub_140001060("wrong input!\n");
			exit(0);
		}
	}
	return tmp1;
}
int sub_1400011E0(char* arg1) {
	int counter = 0;
	int tmp1 = sub_1400010C0(arg1[counter]);
	counter++;
	while(arg1[counter]) {
		int tmp3 = arg1[counter];
		int tmp4 = sub_1400010C0(arg1[counter + 1]);
		switch(tmp3){
			case 'a': tmp1 += tmp4; break;
			case 'd': tmp1 *= tmp4; break;
			case 'f': tmp1 /= tmp4; break;
			case 's': tmp1 -= tmp4; break;
		}
		counter += 2;
	}
	return tmp1 == 0x5b;
}
int main(){
	char* buf = malloc(0x10);
	memset(buf, 0, 0x10);
	sub_140001060("input: "); // sub_140001060 is function like printf
	buf[0] = _fgetchar();
	buf[1] = 'd';
	buf[2] = 'w';
	buf[3] = 's';
	buf[4] = 'q';
	buf[5] = 'a';
	buf[6] = 'w';
	buf[7] = 'd';
	buf[8] = 'u';
	if(sub_1400011E0(buf)) {
		puts("correct!");
	}
	else {
		puts("wrong!");
	}
	return 0;
}