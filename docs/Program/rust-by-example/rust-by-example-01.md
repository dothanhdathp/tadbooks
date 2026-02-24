# Hello World

## Hello World

Đây là mã nguồn của truyền thống `Hello World` chương trình.

```rust
// This is a comment, and is ignored by the compiler.
// You can test this code by clicking the "Run" button over there ->
// or if you prefer to use your keyboard, you can use the "Ctrl + Enter"
// shortcut.

// This code is editable, feel free to hack it!
// You can always return to the original code by clicking the "Reset" button ->

// This is the main function.
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World!");
}
```

`println!` là một macro in văn bản vào bảng điều khiển.

Một nhị phân có thể được tạo bằng cách sử dụng ___Rust compiler___: `rustc`.

```bash
rustc hello.rs
```

Chạy chương trình để xem kết quả:

```text
$ ./hello
Hello World!
```

## Comments

Bất kỳ chương trình nào cũng cần có ý kiến và Rust hỗ trợ một vài loại hoặc kiểu khác nhau trong một nhóm hoặc danh mục lớn hơn khác nhau:

- _Regular comments_ bị bỏ qua bởi trình biên dịch:
    ```rust
    // Line comments which go to the end of the line.
    /* Block comments which go to the closing delimiter. */
    ```

- Nhận xét của tài liệu được phân tích cú pháp vào tài liệu thư viện [documentation](rust-by-example-24.md#documentation):
    ```rust
    /// Generate library docs for the following item.
    //! Generate library docs for the enclosing item.
    ```

!!! info "Info"
    Thư viện [documentation](rust-by-example-24.md#documentation) là thư viện dùng để tạo tài liệu của `cargo`

Phần _bình luận_ như sau:

```rust 
fn main() {
    // This is an example of a line comment.
    // There are two slashes at the beginning of the line.
    // And nothing written after these will be read by the compiler.

    // println!("Hello, world!");

    // Run it. See? Now try deleting the two slashes, and run it again.

    /*
    * This is another type of comment, a block comment. In general,
    * line comments are the recommended comment style. But block comments
    * are extremely useful for temporarily disabling chunks of code.
    * /* Block comments can be /* nested, */ */ so it takes only a few
    * keystrokes to comment out everything in this main() function.
    * /*/*/* Try it yourself! */*/*/
    */

    /*
    Note: The previous column of `*` was entirely for style. There's
    no actual need for it.
    */

    // Here's another powerful use of block comments: you can uncomment
    // and comment a whole block by simply adding or removing a single
    // '/' character:

    /* <- add another '/' before the 1st one to uncomment the whole block

    println!("Now");
    println!("everything");
    println!("executes!");
    // line comments inside are not affected by either state

    // */

    // You can manipulate expressions more easily with block comments
    // than with line comments. Try deleting the comment delimiters
    // to change the result:
    let x = 5 + /* 90 + */ 5;
    println!("Is `x` 10 or 100? x = {}", x);
}
```

## Formatted print

In đầu ra được xử lý bởi một loạt các `macros` được xác định trong `std::fmt` Một số trong đó là:

- `format!`: Viết văn bản được định dạng vào String
- `print!`: Giống như `format!` Nhưng văn bản được in ra _console_ (`io::stdout`).
- `println!`: Giống như `print!` Nhưng một dòng mới được thêm vào.
- `eprint!`: Giống như `print!` nhưng văn bản được in ra lỗi tiêu chuẩn (`io::stderr`).
- `eprintln!`: Giống như `eprint!` nhưng <u>một dòng mới</u> được thêm vào.

```rust
fn main() {
    // In general, the `{}` will be automatically replaced with any
    // arguments. These will be stringified.
    println!("{} days", 31);

    // Positional arguments can be used. Specifying an integer inside `{}`
    // determines which additional argument will be replaced. Arguments start
    // at 0 immediately after the format string.
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

    // As can named arguments.
    println!("{subject} {verb} {object}",
            object="the lazy dog",
            subject="the quick brown fox",
            verb="jumps over");

    // Different formatting can be invoked by specifying the format character
    // after a `:`.
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c

    // You can right-justify text with a specified width. This will
    // output "    1". (Four white spaces and a "1", for a total width of 5.)
    println!("{number:>5}", number=1);

    // You can pad numbers with extra zeroes,
    println!("{number:0>5}", number=1); // 00001
    // and left-adjust by flipping the sign. This will output "10000".
    println!("{number:0<5}", number=1); // 10000

    // You can use named arguments in the format specifier by appending a `$`.
    println!("{number:0>width$}", number=1, width=5);

    // Rust even checks to make sure the correct number of arguments are used.
    println!("My name is {0}, {1} {0}", "Bond");
    // FIXME ^ Add the missing argument: "James"

    // Only types that implement fmt::Display can be formatted with `{}`. User-
    // defined types do not implement fmt::Display by default.

    #[allow(dead_code)] // disable `dead_code` which warn against unused module
    struct Structure(i32);

    // This will not compile because `Structure` does not implement
    // fmt::Display.
    // println!("This struct `{}` won't print...", Structure(3));
    // TODO ^ Try uncommenting this line

    // For Rust 1.58 and above, you can directly capture the argument from a
    // surrounding variable. Just like the above, this will output
    // "    1", 4 white spaces and a "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
```

`std::fmt` chứa một vài `traits` chi phối việc hiển thị văn bản. Hình thức cơ sở của hai cái quan trọng được liệt kê dưới đây:

- `fmt::Debug:` Sử dụng `{:?}` làm dấu. Định dạng văn bản cho mục đích __gỡ lỗi__.
- `fmt::Display`: Sử dụng `{}` làm dấu. Định dạng văn bản Trong một thời trang thanh lịch, thân thiện hơn với người dùng.

Ở đây, chúng tôi đã sử dụng `fmt::Display` Vì thư viện STD cung cấp các triển khai cho các loại này. Để in văn bản cho các loại tùy chỉnh, cần có nhiều bước hơn.

Thực hiện `fmt::Display` Đặc điểm tự động thực hiện `ToString trait` cho phép chúng tôi chuyển đổi loại thành `String`.

Xếp hàng 43, `#[allow(dead_code)]` là một thuộc tính chỉ áp dụng cho _module_ sau nó.