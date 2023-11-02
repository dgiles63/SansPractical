// pageObjects/CoursesPage.js
class CoursesPage {
    visit() {
        cy.visit('https://www.sans.org/cyber-security-courses/?per-page=10');
    }

    applyFocusAreaFilter() {
        cy.get('.checkbox').contains('Cloud Security').check();
    }

    applySkillLevelFilter() {
        cy.get('.checkbox').contains('Advanced (500-699)').check()
    }

    assertResults() {
        cy.get('.results-pane').should('contain', 'SEC488: Cloud Security Essentials');
        cy.get('.results-pane').should('contain', 'SEC540: Cloud Security and DevSecOps Automation');
    }
}

/*  Testing Methodologies
 There are many ways to devise a test plan that would test the matrices of checkbox filters
 to generate results that would give a team confidence in the functionality of the system.
 Those could include:
 1. Random Sampling. Choose 5 to 8 randomly selected combinations, choosing judiciously to cover as many
    individual checkmarks as possible.
 2. Pareto Chart (marketing driven). Agile development has a market driver. Use data to determine
    the most popular purchases and put the emphasis on selections that contain those elements.
 3. Domain Knowledge Testing. Get advice from those who have the most experience with the app as to which
    elements are the most strategic.
 4. The other methodologies include: Endpoint testing (firsts and lasts, gaps and null, etc.), Regression
    based (using past failures to determine what needs the most attention), Latest and Greatest (emphasis
    on the latest additions to the code), Risk-Based (which selections might be the riskiest?), Usability
    Based (What are the most likely selections that users will make based on ease of use)

 What determines the best methodology is whatever the team selects. But let that selection be based on 
 some criteria or objective so that the testing has a purpose and measurable results and can be revised
 to better meet the purpose or objective.

*/