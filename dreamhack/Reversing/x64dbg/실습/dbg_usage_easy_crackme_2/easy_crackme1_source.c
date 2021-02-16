// 컴파일은 visual studio 2019를 통해 하였으며 x64 릴리즈 모드의 옵션은 다음과 같습니다.

// C/C++
// 최적화: 사용 안 함(/Od)
// SDL 검사: 아니요(/sdl-)
// 링커
// 임의 기준 주소: 아니요(/DYNAMICBASE:NO)
// 이외의 옵션은 기본값을 사용하였습니다.

#include <stdio.h>
int numberConvert(char in) {
    int ret = 0;

    switch(in){
        case 'q': ret = 1; break;
        case 'w': ret = 2; break;
        case 'e': ret = 3; break;
        case 'r': ret = 4; break;
        case 't': ret = 5; break;
        case 'y': ret = 6; break;
        case 'u': ret = 7; break;
        case 'i': ret = 8; break;
        case 'o': ret = 9; break;
        case 'p': ret = 0; break;
        default:{
            printf("wrong input!\n");
            exit(0);
        }
    }

    return ret;
}

int check(unsigned char *input) {
    int index = 0;
    int now = numberConvert(input[index]);
    index++;
    
    while(input[index]) {
        int operation = input[index];
        int number = numberConvert(input[index+1]);

        switch(operation) {
            case 'a': now += number; break;
            case 's': now -= number; break;
            case 'd': now *= number; break;
            case 'f': now /= number; break;
            case '\0':break;
        }
        index += 2;
    }

    return now == 105;
}

int main(){
    unsigned char *input = malloc(0x10);
    memset(input, 0, 0x10);

    printf("input: ");

    input[0] = getchar();
    input[1] = 'd';
    input[2] = 'w';
    input[3] = 's';
    input[4] = 'q';
    input[5] = 'a';
    input[6] = 'w';
    input[7] = 'd';
    input[8] = 'u';

    if (check(input)) {
        puts("correct!");
    }
    else {
        puts("wrong!");
    }
}