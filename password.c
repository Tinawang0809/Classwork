#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>


int main(void)
{
    //get the input of password from the user
    string password = get_string("Enter your password: ");

    //preset the names
    bool upper=0,lower=0,number=0,symbol=0;

    //verify whether the password contain uppercase, lowercase, number, and symbol
    int t;
    for(int i=0;i<strlen(password);i++) //find the length of the password, verify the characters one by one
    {
        t=(int)password[i];
        if(t>=65&&t<=90)
            upper=1;
        else if(t>=97&&t<=122)
            lower=1;
        else if(t>=48&&t<=57)
            number=1;
        else if((t>=33&&t<=47)||(t>=58&&t<=64)||(t>=91&&t<=96)||(t>=123&&t<=127))
            symbol=1;
        if(upper==1&&lower==1&&number==1&&symbol==1){
            printf("Your password is valid\n");
            return 0;
        }
    }
    printf("Your password needs at least one uppercase letter, one lowercase letter, number and symbol!\n");
    return 0;

}

