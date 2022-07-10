## Aquest és l'únic document en català la resta de cometaris de codi són en angles
> ### Aquest document té com a objectiu fer una ràpida explicació per entendre que fa cada carpeta dintre del projecte
### BankFunctions
- andBank
    > Funcionalitats del banc Andbank actualment. Ja un script per obtenir el missatge de confirmació del telèfon i un altre que interactua amb els elements de la web per executar el inici de sessió en si.
- apiFunctions
    - templates
        > Disposem de dos html, ***idex*** és per crear credencials i guardar-les encriptades.
    ***Checktotals*** és per utilitzar tant per consultar totals com per realitzar una transferència.
    > ***apiEndpoints*** És senzillament una declaració d'enpoints per poder accedir a les funcionalitats de forma remota.
També ens retorna els HTML a dintre de templates
- credit
    > ***confirmatonCodeCredit*** És un script que ens permet obtenir tant el missatge de confirmació per realitzar una transacció com el missatge per fer l'inici de sessió a la plana web. Aquest no són iguals.

    > ***coordenatesFlow*** És el flow que s'utilitzava per realitzar entrar l'informació de la targeta de coordenades, però aquesta funcionalitat ha sigut donada de baixa pel bank.

    > ***downloadExpenses*** Consisteix a controlar la web per descarregar els totals dels comptes bancari

    > ***loginAndNavegateCredit*** Aquest flux consisteix a fer un inici de sessió al banc utilitzant la web

    > ***makeTransfer*** Aquest flux consisteix a fer una transferència al banc utilitzant la web
- emailFunctionalties
    > Utilitza imap per extreure l'últim email rebut aka el missatge de confirmació que IFTTT envia en rebre un missatge al telèfon.
- encryptionFunctionalties
    > ***encryptFileUsingKey*** Encripta les credencials utilitzant una clau i destrueix el contingut sense encriptar

    > ***encryptionKeyGeneration*** Genera una clau a utilitzar per a l'encriptació

    > ***generateKeyAndUseIT*** Genera la clau i l'utilitza per encriptar

    > ***readEncryptedFileModulus*** Llegeix un document encriptat utilitzant una clau i retorna l'informació en format JSON
- rasaConnections
    > ***catalaConnectionText*** Envia un missatge per veu és processar acordament i retorna una resposta en text
    
    > ***catalaConnectionVoiceResonse*** Envia un missatge per veu és processar acordament i retorna una resposta en veu

    > ***terminalTriggers*** Connexió amb l'interpretador sintàctic tot per text
### RasaProject
- actions
    > Ara mateix no s'està utilitzant per res per es pot utilitzar per executar funcionalitats de Python costum en el context del interpretador.

- data
    > ***nlu*** És un document declaratiu que és utilitzat per entrenar la nostra xarxa neuronal, consisteix d'un seguit d'exemples, dels que definiríem com intencions de l'usuari, l'objectiu és classificar l'input de l'usuari basat en aquesta classificació d'intencions

    > ***rules*** És un document que es salta les pautes establertes a les històries per donar una resposta fora de context. És important ser conscient que això pot impactar negativament les funcionalitats del programa si es fa un ús abusiu

    > ***stories*** Aquest document serveix per guiar una conversa amb el programa és a dir com s'haurà de respondre a detecció de les intencions del programa. I quines variacions podria tenir aquesta conversa.
- models
    > Es guarda el resultat de l'entrenament de les xeixes neuronals
- test
    > històries de prova per comprovar el funcionament de la xarxa neuronal
- Resta de documents
    > ***config*** És el document que ens permet realitzar les configuracions del programa, ara mateix està configurat perquè interactiu amb una instància de [duckling](https://github.com/facebook/duckling)  que està funcionat localment en un container de docker.

    > ***credentials*** Ara mateix només s'està utilitza'n per declarar l'endpoint de connexió.
    Però es pot utilitzar per fer verificació d'usuaris connexions segures, etc

    > ***domain*** És un document que serveix per declarar entitats slots de memòria (perquè el programa pugui recordar coses) i respostes a disposar.

    > ***endpoints*** Per realitzar altres tipus de connexions no s'està utilitzant actualment

### Nota he hagut d'eliminar els models neuronals i altres log files per poder pujar el document