public class App {
    public static void main(String[] args) throws Exception {
        Carro carro1 = new Carro("Skyline GTR", "Azul", 1999);

        System.out.println("Minha garagem:");
        System.out.println("> " + carro1.modelo + " - " + carro1.cor + " - " + carro1.ano + ";");
    }
}
