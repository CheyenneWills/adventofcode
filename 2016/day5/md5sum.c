#include <openssl/md5.h>
#include "icall.h"

int MD5sum(int argc,descriptor argv[])  
{
    MD5_CTX c;
    char *s;      
    int slen;
    unsigned char out[MD5_DIGEST_LENGTH];

    MD5_Init(&c);
    ArgString(1);
    
    s = StringAddr(argv[1]);
    slen = StringLen(argv[1]);
    MD5_Update(&c,s,slen);
    MD5_Final(out,&c);
    RetStringN(out,MD5_DIGEST_LENGTH);
}
