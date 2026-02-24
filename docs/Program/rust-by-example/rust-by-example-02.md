# Primitives

> Nguồn: [https://doc.rust-lang.org/rust-by-example/primitives.html](https://doc.rust-lang.org/rust-by-example/primitives.html)
## Primitives

> __*primitives*__: Các kiểu biến cơ bản (kiểu biến nguyên thuỷ). Là tập hợp gồm các loại biến có sẵn, được hỗ trợ trực tiếp bởi trình biên dịch mà không cần thông qua một hình thức khai báo nào.

Rust cung cấp quyền truy cập vào nhiều loại cơ bản. Một ví dụ cơ bản:

### Scalar _(vô hướng)_

- Số nguyên có dấu: `i8`, `i16`, `i32`, `i64`, `i128` và `isize` _(kích thước của con trỏ)_
- Số nguyên không dấu _(không âm)_: `u8`, `u16`, `u32`, `u64`, `u128` và `usize` _(kích thước của con trỏ không âm)_
- Số thực: `f32`, `f64`
- `char` Unicode scalar values like 'a', 'α' and '∞' (4 bytes each)
- `bool` hoặc `true` hoặc `false`
- Loại đơn vị `()`, có giá trị duy nhất có thể là một `tuple`: `()`. _(Tập hợp của nhiều dữ liệu)_

Mặc dù giá trị của loại đơn vị là một bộ, nhưng nó không được coi là loại kết hợp vì nó không chứa nhiều giá trị.

### Compound Types (Loại phức hợp)

- __Arrays__: `[1, 2, 3]`
- __Tuples__: `(1, true)`

Các biến có thể luôn được kèm annotated _(chú thích)_. Ngoài ra, các số có thể được chú thích thông qua hậu tố hoặc mặc định. Các số nguyên mặc định là `i32` và số thực là `f64`. Lưu ý rằng Rust cũng có thể nội suy ra các kiểu dữ liệu từ ngữ cảnh.

```rust
fn main() {
    // Variables can be type annotated.
    let logical: bool = true;

    let a_float: f64 = 1.0;  // Regular annotation
    let an_integer   = 5i32; // Suffix annotation

    // Or a default will be used.
    let default_float   = 3.0; // `f64`
    let default_integer = 7;   // `i32`

    // A type can also be inferred from context.
    let mut inferred_type = 12; // Type i64 is inferred from another line.
    inferred_type = 4294967296i64;

    // A mutable variable's value can be changed.
    let mut mutable = 12; // Mutable `i32`
    mutable = 21;

    // Error! The type of a variable can't be changed.
    mutable = true;

    // Variables can be overwritten with shadowing.
    let mutable = true;

    /* Compound types - Array and Tuple */

    // Array signature consists of Type T and length as [T; length].
    let my_array: [i32; 5] = [1, 2, 3, 4, 5];

    // Tuple is a collection of values of different types
    // and is constructed using parentheses ().
    let my_tuple = (5u32, 1u8, true, -5.04f32);
}
```

- __*Liên kết tham khảo:*__: [the std library](https://doc.rust-lang.org/std/), [mut](https://doc.rust-lang.org/rust-by-example/variable_bindings/mut.html), [inference](https://doc.rust-lang.org/rust-by-example/types/inference.html), và [shadowing](https://doc.rust-lang.org/rust-by-example/variable_bindings/scope.html)

## Literals and operators

> Ký Tự và Toán Tử

Integers 1, floats 1.2, characters 'a', strings "abc", booleans true and the unit type () can be expressed using literals.

Integers can, alternatively, be expressed using hexadecimal, octal or binary notation using these prefixes respectively: 0x, 0o or 0b.

Underscores can be inserted in numeric literals to improve readability, e.g. 1_000 is the same as 1000, and 0.000_001 is the same as 0.000001.

Rust also supports scientific E-notation, e.g. 1e6, 7.6e-4. The associated type is f64.

We need to tell the compiler the type of the literals we use. For now, we'll use the u32 suffix to indicate that the literal is an unsigned 32-bit integer, and the i32 suffix to indicate that it's a signed 32-bit integer.

The operators available and their precedence in Rust are similar to other C-like languages.

