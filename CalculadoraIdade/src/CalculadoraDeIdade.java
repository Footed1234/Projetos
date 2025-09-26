import java.util.Scanner;

public class CalculadoraDeIdade {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        final int ANO_ATUAL = 2025;

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite o ano em que você nasceu: ");
        int anoNascimento = scanner.nextInt();

        int idade = ANO_ATUAL - anoNascimento;

        System.out.println("Olá, " + nome + "! Você tem " + idade + " anos.");

        scanner.close();
    }
}


