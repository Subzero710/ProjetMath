import matplotlib.pyplot as plt
from main import SimulateurTraitement, exoObligatoireMoyenne, exoFacultatif1Mono, exoFacultatif1Moyenne, \
    exo1VariantMoyenne


def plot_success_tracking(tracking):
    plt.plot(tracking)
    plt.title("Succès cumulés moyens")
    plt.xlabel("Patients")
    plt.ylabel("Succès cumulés")
    plt.grid(True)
    plt.show()

def plot_success_rates(rates):
    traitements = ['A', 'B', 'C', 'D', 'E']
    plt.bar(traitements, rates)
    plt.title("Taux de succès moyen par traitement")
    plt.ylabel("Taux de succès")
    plt.ylim(0, 1)
    plt.grid(axis="y")
    plt.show()

def plot_proportions(proportions):
    traitements = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        plt.plot([p[i] for p in proportions], label=traitements[i])
    plt.title("Nombre cumulé moyen de traitements utilisés")
    plt.xlabel("Patients")
    plt.ylabel("Utilisations cumulées")
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    simulator = SimulateurTraitement()
    #mean_total_success, mean_success_tracking, mean_success_rates, mean_proportions = exoObligatoireMoyenne(simulator,1000)
    #total_success, success_tracking, success_rates, proportions = exoFacultatif1Mono(simulator,1000)
    #total_success, success_tracking, success_rates, proportions = exoFacultatif1Moyenne(simulator,1000)
    total_success, success_tracking, success_rates, proportions = exo1VariantMoyenne(simulator, 1000)
    print(f"Succès total moyen : {total_success:.2f}")
    plot_proportions(proportions)
    plot_success_tracking(success_tracking)
    plot_success_rates(success_rates)
