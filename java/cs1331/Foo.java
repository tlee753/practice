@FunctionalInterface
public interface Foo {
    
    String bar(Object o);

    static String baz(Object o) {
        return o.toString();
    }
}
