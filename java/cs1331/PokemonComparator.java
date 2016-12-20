import java.util.Comparator;

public class PokemonComparator implements Comparator<Pokemon> {
  public int compare(Pokemon pokeOne, Pokemon pokeTwo) {
    //return pokeTwo.getWeight() - pokeOne.getWeight();
    return pokeOne.getType().ordinal() - pokeTwo.getType().ordinal(); // ordinal is a method that returns position in enum
  }
}
