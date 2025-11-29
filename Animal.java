package IMPORTANT;
class Animal {
    int x=20;
    Animal ( String type){
        System.err.println("The type of animal is: " + type);
    }
    void show() {
        System.out.println("I am a parent class method.");
    }
}
class Dog extends Animal{
    int x=30;
    Dog(String type){
        super(type);
    }
    void show() {
        super.show();
        System.out.println("super class variable x is:" + super.x);
        System.out.println("child class variable x is:" + this.x);
        System.out.println("I am a child class method.");
    }
}
class inheritance{
    public static void main(String[] args) {
        Dog d=new Dog("Mammal");
        d.show();
        System.out.println(d.x);
    }
}