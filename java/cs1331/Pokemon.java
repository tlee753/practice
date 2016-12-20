import java.util.ArrayList;
import java.util.Collections;

public class Pokemon implements Comparable<Pokemon> {
  private int weight;
  private Types type;

  public enum Types {
    WATER, FIRE, GRASS, ELECTRIC;
  }

  public Pokemon(int weight, Types type) {
    this.weight = weight;
    this.type = type;
  }

  public int compareTo(Pokemon other) {
    return this.weight - other.weight;
  }

  public String toString() {              // overrides object's toString method
    return this.weight + ":" + this.type;
  }

  public int getWeight() {
    return weight;
  }

  public Types getType() {
    return type;
  }

  public static void main(String[] args) {
    Pokemon pikachu = new Pokemon(12, Types.ELECTRIC);
    Pokemon charmander = new Pokemon(8, Types.FIRE);
    Pokemon squirtle = new Pokemon(10, Types.WATER);
    Pokemon bulbasaur = new Pokemon(14, Types.GRASS);
    // System.out.println(pikachu.compareTo(charmander));
    ArrayList<Pokemon> myPokes = new ArrayList<>(); // using pokemon type
    myPokes.add(pikachu);
    myPokes.add(charmander);
    myPokes.add(squirtle);
    myPokes.add(bulbasaur);
    System.out.println(myPokes);
    PokemonComparator comparatorOne = new PokemonComparator();
    Collections.sort(myPokes, comparatorOne); // use comparator here
    System.out.println(myPokes);
  }
}
