class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }

    public void sleep() {
        System.out.println(name + " is sleeping.");
    }
}

class Bird extends Animal {
    private String featherColor;

    public Bird(String name, String featherColor) {
        super(name);
        this.featherColor = featherColor;
    }

    public void fly() {
        System.out.println(name + " with " + featherColor + " feathers is flying.");
    }
}

class Parrot extends Bird {
    public Parrot() {
    }
}

class Fish extends Animal {
    private String habitat;

    public Fish(String name, String habitat) {
        super(name);
        this.habitat = habitat;
    }

    public void swim() {
        System.out.println(name + " is swimming in " + habitat + ".");
    }
}
class RedFish extends Fish {
    public RedFish() {
    }
}

class Mammal extends Animal {
    private int legs;

    public Mammal(String name, int legs) {
        super(name);
        this.legs = legs;
    }

    public void walk() {
        System.out.println(name + " is walking on " + legs + " legs.");
    }
}
class Human extends Mammal {
    public Human() {
    }
}

class Panda extends Mammal {
    public Panda() {
    }
}

class Bat extends Mammal {
    public Bat() {
    }
}
public class Main {
    public static void main(String[] args) {
    }
}
