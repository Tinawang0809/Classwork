/*
Demical to binary, octal，and hexadecimal
ask user for base number
1 function (number, base)
allow the user to convert
*/



#include <cs50.h>
#include <stdio.h>
#include <math.h>

void convert(long x, int base);

int arr[1000]; //array to store the remainder

char hex[16]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E'};//hex chart

int main(void)
{
    long n;
    char check;
    bool repeat=1;

    while(repeat)// repeat prompt
    {
        n=get_long("Enter a demical number:");// ask for input

        //call function
        convert(n,2);
        convert(n,8);
        convert(n,16);

        check = get_char("Do you want to convert another number? Y/N");
        if(check == 'N' || check == 'n')
        {
            repeat=0; //when repeat=0, it will not return to the previous while function, and the algorithm will end
        }
    }

    }

    void convert(long x, int base)// specify the function: to define what is long x and int base
{
        int digit =0;

        while (x>0)
        {
            arr[digit]=x%base; //mod base,calculate remainder
            digit++;
            x=x/base;// divide for the next number
        }


    if(base==2)
    {
        printf("Binary: \n");
    }

    if(base==8)
    {
        printf("Octal: \n");
    }

    if(base==16)
    {
        printf("Hexidecimal: \n");

    }


    for (int i=digit-1; i>=0; i--)// print in reverse order
    {
        printf("%c", hex[arr[i]]);
    }
    printf("/n");
}
