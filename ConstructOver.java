class ConstructOver {
    public static void main(String[] args) {
        
    }
    ConstructOver(String name){
        ConstructorOverloading(String name,int age){
            this.name=name;
            this.age=age;

        }
        void display(){
            System.out.println
        }
    }
}

class Loop{
    public static void main(String[] args) {
        ConstructOver obj=new ConstructOver();
        ConstructOver obj2=new ConstructOver("Utsav");
        ConstructOver obj3=new ConstructOver("Utsav" , 20);
        obj.display();
        obj2.display();
        obj3.display();
    }
}