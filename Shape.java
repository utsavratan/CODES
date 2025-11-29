package IMPORTANT;

inheritance Printable{
    abstract void print();
    default void defaultMethod(){
        System.out.println("Default method of printable interface");
    }

}
interface Drawable{
    abstract void draw();
    default void defaultMethod(){
        System.out.println("Default method of Drawable interface");
}
}
public class Shape implements Drawable, Printable{
    public void draw(){
        System.out.println("drawing");

    }
    public void print(){
        System.out.println("printing");
    }
    }
}