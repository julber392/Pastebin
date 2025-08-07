#include <cstring>
#include <cstdio>
#include <openssl/evp.h>

extern "C" {

void sha256_c(const char* input, char* output) {
    EVP_MD_CTX* ctx = EVP_MD_CTX_new();
    const EVP_MD* md = EVP_sha256();
    unsigned char hash[EVP_MAX_MD_SIZE];
    unsigned int length = 0;

    EVP_DigestInit_ex(ctx, md, nullptr);
    EVP_DigestUpdate(ctx, input, strlen(input));
    EVP_DigestFinal_ex(ctx, hash, &length);
    EVP_MD_CTX_free(ctx);

    for (unsigned int i = 0; i < length; ++i) {
        snprintf(output + i * 2, 3, "%02x", hash[i]);
    }
    output[64] = 0;
}

}
