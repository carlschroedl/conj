//generic load function works for loading data into all simple view models
var loadData = function(data, self) {
    for (prop in data) {
        if (self.hasOwnProperty(prop)) {
            self[prop](data[prop]); //write to the ko.observable
        }
        else {
            console.log('Warning: object does not have a property named "' + prop + '".');
        }
    }
};

//<view models>
var Document = function() {
    var self = this;
    self.id = ko.observable();
    self.parseId = ko.observable();
    self.title = ko.observable();
    self.nonfiltered = ko.observable();
    self.processed = ko.observable();
    self.parseDbIndex = ko.observable();

    self.loadData = function(data) {
        loadData(data, self);
    };

}


var Sentence = function() {
    var self = this;
    self.id = ko.observable();
    self.document = ko.observable();
    self.text = ko.observable();

    self.loadData = function(data) {
        loadData(data, self);
    };
};


var Verb = function() {
    var self = this;
    self.id = ko.observable();
    self.token = ko.observable();
    self.lemma = ko.observable()
    self.rawTag = ko.observable();
    //moods
    self.indicative = ko.observable();
    self.subjunctive = ko.observable();
    self.imperative = ko.observable();
    self.gerund = ko.observable();
    self.infinitive = ko.observable();
    self.participle = ko.observable();
    //tenses
    self.present = ko.observable();
    self.preterite = ko.observable();
    self.imperfect = ko.observable();
    self.conditional = ko.observable();
    self.future = ko.observable();
    //conjugation pattern
    self.irregular = ko.observable();
    //frequency
    self.frequent = ko.observable();
    //person
    self.firstPerson = ko.observable();
    self.secondPerson = ko.observable();
    self.thirdPerson = ko.observable();
    //plurality
    self.singular = ko.observable();
    self.plural = ko.observable();





    self.loadData = function(data) {
        loadData(data, self);
    };

};

var Exercise = function() {
    var self = this;
    self.id = ko.observable();
    self.verbLocation = ko.observable();
    self.sentence = ko.observable(new Sentence());
    self.verb = ko.observable(new Verb());
    self.flagCount = ko.observable();

    self.userWasCorrect = ko.observable(); //boolean
    self.userWasWrong = ko.computed(function(){
        return self.userWasCorrect() != undefined && !self.userWasCorrect();
    });
    self.startExercise = ko.observable(true);

    self.userAnswer = ko.observable();  //text supplied by user
    
    //don't attempt to modify these arrays directly, use
    //their corresponding mutators below
    self.leftHalf = ko.observableArray();
    self.rightHalf = ko.observableArray();

    self.updateLeftHalf = ko.computed(function() {
        if ( 'undefined' != typeof self.sentence() &&
             'undefined' != typeof self.verbLocation() &&
             'undefined' != typeof self.sentence().text()) {
            var verbLoc = self.verbLocation();
            if (verbLoc != 0) {
                verbLoc -= 1;
                //-1 for the space preceding the verb
            }
            var leftText = self.sentence().text().slice(0, verbLoc);

            var wordArray = leftText.split(' ');
            //clear the array bound to the UI and add new things
            self.leftHalf.removeAll();
            ko.utils.arrayForEach(wordArray, function(word) {
                self.leftHalf.push(word);
            });
        }
    });

    self.updateRightHalf = ko.computed(function() {
        if ( 'undefined' != typeof self.sentence() &&
             'undefined' != typeof self.verbLocation() &&
             'undefined' != typeof self.sentence().text()) {
            var verbEndLoc = self.verbLocation() + self.verb().token().length + 1;
            //+1 for the space following the verb
            var rightText = self.sentence().text().slice(verbEndLoc);

            var wordArray = rightText.split(' ');
            //clear the array bound to the UI and add new things
            self.rightHalf.removeAll();
            ko.utils.arrayForEach(wordArray, function(word) {
                self.rightHalf.push(word);
            });
        }
    });

    //<info functions> @todo eliminate repetition
    self.personInfo = ko.computed(function(){
        var person = ''
        if('undefined' != typeof self.verb()){
            //map verb property name to displayed text
            var personMap = {
                firstPerson: 'first person',
                secondPerson: 'second person',
                thirdPerson: 'third person',
            };
            //set 'person' according to the properties in self.verb()
            for (prop in personMap) {
                if (self.verb()[prop]()) {
                    person = personMap[prop];
                    break;
                }
            }   
        }
        return person;
    });
    self.pluralityInfo = ko.computed(function(){
        var plurality = ''
        if('undefined' != typeof self.verb()){
            //map property name to displayed text
            var pluralityMap = {
                singular: 'singular',
                plural: 'plural'
            };
            //set return value according to the properties in self.verb()
            for (prop in pluralityMap) {
                if (self.verb()[prop]()) {
                    plurality = pluralityMap[prop];
                    break;
                }
            }   
        }
        return plurality;
    });
    self.moodInfo = ko.computed(function(){
        var mood = ''
        if('undefined' != typeof self.verb()){
            //map property name to displayed text
            var moodMap = {
                'indicative': 'indicative',
                'subjunctive': 'subjunctive',
                'imperative': 'imperative',
                'gerund': 'gerund',
                'infinitive': 'infinitive',
                'participle': 'participle'
            };
            //set return value according to the properties in self.verb()
            for (prop in moodMap) {
                if (self.verb()[prop]()) {
                    mood = moodMap[prop];
                    break;
                }
            }   
        }
        return mood;
    });
    self.tenseInfo = ko.computed(function(){
        var tense = ''
        if('undefined' != typeof self.verb()){
            //map property name to displayed text
            var tenseMap = {
                'present': 'present',
                'preterite': 'preterite',
                'imperfect': 'imperfect',
                'conditional': 'conditional',
                'future': 'future'
            };
            //set return value according to the properties in self.verb()
            for (prop in tenseMap) {
                if (self.verb()[prop]()) {
                    tense = tenseMap[prop];
                    break;
                }
            }   
        }
        return tense;
    });

    //</info functions>
    self.loadData = function(data) {
        loadData(data, self);
    };
    
    self.checkAnswer = function(){
       if('undefined' !== typeof self.userAnswer()){
        
       if(self.userAnswer().toLowerCase() === self.verb().token().toLowerCase()){
           self.userWasCorrect(true);
       }
       else{
           self.userWasCorrect(false);
           self.startExercise(true);
       }
       }
    }
    self.getNewExercise = function(){
        //@todo convert this into a post that send data to the server
        self.userWasCorrect(undefined);
        self.userAnswer(undefined);
        $.get("/exercise/", function(data) {
            data = data[0]
            //$("#success").fadeIn();
            console.dir(data);
            //shuffle the data around into the right spots
            var exerciseData = data.fields;
            exerciseData.id = data.pk;
            
            //<simplify> @todo this can be done with the knockout mapping plugin
            sentenceData = exerciseData.sentence;
            verbData = exerciseData.verb;
            var s = new Sentence();
            s.loadData(sentenceData);
            var v = new Verb();
            v.loadData(verbData);
            //overwrite 
            exerciseData.sentence = s;
            exerciseData.verb = v;
            //</simplify
            
            sentenceData = exerciseData.sentence;
            self.loadData(exerciseData);
            self.startExercise(true);
        });
    };
    
};

//</view models>
//<temporary viewModel tests>
//normally the ajax calls will provide the arguments for the loadData calls.
//use literals here for simplicity
//use the same document for all tests; none of the doc stuff is displayed

//var d = new Document();


/* <test1>
//tests verb in the middle of the sentence
var v1 = new Verb();

v1.loadData({
    irregular: 0,
    indicative: 1,
    present: 1,
    id: 42,
    token: 'conjugo',
    lemma: 'conjugar'
});

var s1 = new Sentence();

s1.loadData({
    id: 1,
    document: d,
    text: "Yo no conjugo los verbos ."
});

var x1 = new Exercise();
x1.loadData({
    id: 2,
    sentence: s1,
    verb: v1,
    verbLocation: 6
});
ko.applyBindings(x1);
//</test1> */

/* <test2>
//tests verb at the very front of the sentence
var v2 = new Verb();

v2.loadData({
    irregular: 0,
    indicative: 1,
    present: 1,
    id: 42,
    token: 'Conjugo',
    lemma: 'conjugar'
});

var s2 = new Sentence();

s2.loadData({
    id: 1,
    document: d,
    text: "Conjugo los verbos ."
});

var x2 = new Exercise();
x2.loadData({
    id: 2,
    sentence: s2,
    verb: v2,
    verbLocation: 0
});
ko.applyBindings(x2);
// </test2> */
/*<test3>
//tests verb at end of sentence (but before terminal punctuation)
var v3 = new Verb();

v3.loadData({
    irregular: 0,
    subjunctive: 1,
    present: 1,
    id: 42,
    token: 'conjuegen',
    lemma: 'conjugar'
});

var s3 = new Sentence();

s3.loadData({
    id: 1,
    document: d,
    text: "Es dudoso que conjuegen ."
});

var x3 = new Exercise();
x3.loadData({
    id: 2,
    sentence: s3,
    verb: v3,
    verbLocation: 14
});
ko.applyBindings(x3);
//</test3> */


//</temporary viewModel tests>
