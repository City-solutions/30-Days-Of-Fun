package Day7;

public class Animal {

    public String name;

    public void eat() {
        System.out.println("I am eating");
    }

    // set name
    public void setName(String name) {
        this.name = name;
    }

    
    public static void main(String[] args){

        Animal cat =  new Animal();
        cat.setName("Tom");
        System.out.println(cat.name);

        Animal dog = new Animal();
        dog.setName("Jerry");
        System.out.println(dog.name);

    }
    
}


