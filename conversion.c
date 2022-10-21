#include <cs50.h>
#include <stdio.h>
#include <math.h>

int getnum();
int conversion();
int result();

int main(void)
{
    int input=getnum();

}

int getnum()
{
    int input=0;
    do
    {
        input=get_int("Please enter a number");
    }
    while(input<0);
    return input;
}

void conversion()
{

}
