fn fib(n: i32) -> i32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib(n - 1) + fib(n - 2)
    }
}

#[no_mangle]
pub extern fn fibonacci(n: i32) -> i32 {
    let r: i32 = fib(n);
    // println!("Hello, Rust");
    r
}
