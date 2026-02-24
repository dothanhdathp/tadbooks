# Famous Floating Point Problem

## Vấn đề 0.1 + 0.2 khác 0.3?

Về toán học, ai cũng biết rằng $0.1 + 0.2 = 0.3$. Nhưng trong lập trình đây là một bài toán nổi tiếng. Hãy thử một đoạn lập trình nhỏ về một bài toán đơn giản như sau _(ngôn ngữ C)_.

```c
#include "stdio.h"

int main(int argc, char const *argv[]) {
    if((0.1 + 0.2) == 0.3) {
        printf("True");
    } else {
        printf("False");
    }
    return 0; // Return success
}
```

Đoạn chương trình trên thực hiện kiểm thử kết quả của `0.1 + 0.2` và so sánh với `0.3`. Thật kỳ lạ, kết quả trả về __False__.

Đây là bài toán kinh điển và nổi tiếng trong lập trình đến mức có hàng loạt bài viết và cảnh báo về nó, ví dụ như:

- [You can use floating-point numbers for money](https://www.evanjones.ca/floating-point-money.html)
- [What Every Programmer Should Know About Floating-Point Arithmetic](https://floating-point-gui.de/)
- [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
- [Why don’t my numbers, like 0.1 + 0.2 add up to a nice round 0.3, and instead I get a weird result like 0.30000000000000004?](https://floating-point-gui.de/basic/)

## Tại sao?

Đấy không phải là lỗi của máy tính, mà là do cách máy tính thực hiện phép tính liên quan đến dấu phẩy động. Theo lý thuyết, một số thực 

... làm tiếp ...

## Cách giải quyết

Với ngôn ngữ __C__ hoặc __C++__, bắt buộc phải thêm hậu tố xác định vào sau mỗi khai báo số thực nguyên thuỷ. Ví dụ:

```cpp
#include "stdio.h"

using namespace std;

int main(int argc, char const *argv[]) {
    float a = 0.1;
    float b = 0.2;
    float c = 0.3;

    printf("a = %f\n", a);
    printf("b = %f\n", b);
    printf("c = %f\n", c);

    printf(" 0.1 +  0.2 ?=  0.3 : %s\n", ((0.1+0.2)==0.3) ? " true" : "false");
    printf("   a +    b ?=  0.3 : %s\n", (a+b)==0.3 ? " true" : "false");
    printf("          c ?=  0.3 : %s\n", c==0.3 ? " true" : "false");
    printf("   a +    b ?=    c : %s\n", (a+b)==c ? " true" : "false");

    // Giải Quyết:

    printf("0.1f + 0.2f ?= 0.3f : %s\n", ((0.1f+0.2f)==0.3f) ? " true" : "false");
    printf("   a +    b ?= 0.3f : %s\n", (a+b)==0.3f ? " true" : "false");
    printf("          c ?= 0.3f : %s\n", c==0.3f ? " true" : "false");
    printf("   a +    b ?=    c : %s\n", (a+b)==c ? " true" : "false");
    return 0; // Return success
}
```

Kết quả:

```text
a = 0.100000
b = 0.200000
c = 0.300000
 0.1 +  0.2 ?=  0.3 : false
   a +    b ?=  0.3 : false
          c ?=  0.3 : false
   a +    b ?=    c :  true
0.1f + 0.2f ?= 0.3f :  true
   a +    b ?= 0.3f :  true
          c ?= 0.3f :  true
   a +    b ?=    c :  true
```

