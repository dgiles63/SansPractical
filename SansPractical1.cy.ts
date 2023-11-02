import 'cypress-real-events';

// pageObjects/MainMenu.js
class MainMenu {
    visit() {
        cy.visit('https://www.sans.org/');
    }

    hoverTrainAndCertify() {
        cy.get('a').contains('Train and Certify').realHover().then(($el) => {
            setTimeout(() => {
              cy.get('a').contains('Courses').should('be.visible');
              cy.get('a').contains('Courses').realHover().then(($el) => {
                setTimeout(() => {
                    cy.get('a').contains('Full Course List').should('be.visible').click();
                }, 3000); // Adjust the hold duration as needed (in milliseconds)
            });

            }, 6000); // Adjust the hold duration as needed (in milliseconds)
        });

        
    }
}

// // pageObjects/TrainAndCertifyMenu.cy.ts
// class TrainAndCertifyMenu {
//     hoverCourses() {
//         cy.get('a').contains('Courses').realHover();
//         cy.wait(1000);
//     }
// }

// pageObjects/CoursesMenu.cy.ts
class CoursesMenu {
    hoverFullCourseList() {
        cy.get('a').contains('Full Course List').trigger('mouseover', {force: true}).click({force: true});
    }    
}

// pageObjects/AssertClassList.cy.ts
class ClassAssertions {
    assertionListOfClasses() {
        cy.url().should('contain', "https://www.sans.org/cyber-security-courses/");
        
    }
}

// tests/navigation.spec.cy.ts
describe('Navigation', () => {
    it('Navigates through menus', () => {
        const mainMenu = new MainMenu();
        // const trainAndCertifyMenu = new TrainAndCertifyMenu();
        //const coursesMenu = new CoursesMenu();
        const classAssertions = new ClassAssertions();

        mainMenu.visit();
        mainMenu.hoverTrainAndCertify();
        // trainAndCertifyMenu.hoverCourses();
        //coursesMenu.hoverFullCourseList();
        classAssertions.assertionListOfClasses();
        
    });
});


