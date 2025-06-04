import matplotlib.pyplot as plt
from main import SimulateurTraitement, exoObligatoireMoyenne

def plot_success_tracking(tracking):
    plt.plot(tracking)
    plt.title("Succès cumulés moyens (Uniforme)")
    plt.xlabel("Patients")
    plt.ylabel("Succès cumulés")
    plt.grid(True)
    plt.show()

def plot_success_rates(rates):
    traitements = ['A', 'B', 'C', 'D', 'E']
    plt.bar(traitements, rates)
    plt.title("Taux de succès moyen par traitement (Uniforme)")
    plt.ylabel("Taux de succès")
    plt.ylim(0, 1)
    plt.grid(axis="y")
    plt.show()

def plot_proportions(proportions):
    traitements = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        plt.plot([p[i] for p in proportions], label=traitements[i])
    plt.title("Nombre cumulé moyen de traitements utilisés (Uniforme)")
    plt.xlabel("Patients")
    plt.ylabel("Utilisations cumulées")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulator = SimulateurTraitement()
    mean_total_success, mean_success_tracking, mean_success_rates, mean_proportions = exoObligatoireMoyenne(simulator)

    print(f"Succès total moyen : {mean_total_success:.2f}")
    plot_success_tracking(mean_success_tracking)
    plot_success_rates(mean_success_rates)
    plot_proportions(mean_proportions)
